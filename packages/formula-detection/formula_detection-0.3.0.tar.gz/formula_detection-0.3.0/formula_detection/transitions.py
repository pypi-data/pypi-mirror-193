from typing import Dict, List, Set, Union
import copy
from collections import Counter
from collections import defaultdict


def normalise_context(context_words: List[str], variant_of: Dict[str, str]) -> List[str]:
    return [w if w not in variant_of else variant_of[w] for w in context_words]


def select_context_words(phrases: Union[str, List[str]], context_count: Dict[str, Counter],
                         variant_of: Dict[str, str], min_word_prob: float = 0.1) -> List[str]:
    total = 0
    context_word_freq = Counter()
    for phrase in phrases:
        total += sum(context_count[phrase].values())
        for pc in context_count[phrase]:
            norm_pc = normalise_context(pc.split(' '), variant_of)
            for norm_word in set(norm_pc):
                context_word_freq[norm_word] += context_count[phrase][pc]
    selected = []
    for word, freq in context_word_freq.most_common():
        if freq / total < min_word_prob:
            continue
        # print(f'{sub_phrase: <40}{word: <20}{freq: >8}{freq / total: >8.2f}')
        selected.append(word)
    return selected


def prune_branch(curr_node: str, transition_probs: Dict[str, Dict[str, float]], debug: bool = False):
    next_nodes = list(transition_probs[curr_node].keys())
    for next_node in next_nodes:
        if debug:
            print('REMOVING connection', curr_node, next_node)
        del transition_probs[curr_node][next_node]
        prune_branch(next_node, transition_probs)
    del transition_probs[curr_node]
    if debug:
        print('REMOVING leaf', curr_node)
    return None


def prune_word_transitions(transition_probs: Dict[str, Dict[str, float]],
                           min_prob_threshold: float = 0.01, debug: bool = False):
    curr_words = list(transition_probs.keys())
    for curr_word in curr_words:
        next_words = list(transition_probs[curr_word].keys())
        for next_word in next_words:
            if transition_probs[curr_word][next_word] < min_prob_threshold:
                # print('curr:', curr_word, '\tnext:', next_word, '\tprob:', transition_probs[curr_word][next_word])
                del transition_probs[curr_word][next_word]
                # prune_branch(next_word, transition_probs, debug=debug)
    for word in curr_words:
        if word in transition_probs and len(transition_probs[word]) == 0:
            del transition_probs[word]
    return None


def prune_phrase_transitions(transition_probs: Dict[str, Dict[str, float]],
                             min_prob_threshold: float = 0.1, debug: bool = False):
    phrases = sorted(transition_probs.keys(), key=lambda x: len(x))
    for phrase in phrases:
        extended_phrases = list(transition_probs[phrase].keys())
        for extended_phrase in extended_phrases:
            if transition_probs[phrase][extended_phrase] < min_prob_threshold:
                # print(phrase, extended_phrase, transition_probs[phrase][extended_phrase])
                del transition_probs[phrase][extended_phrase]
                prune_branch(extended_phrase, transition_probs, debug=debug)
    for phrase in phrases:
        if phrase in transition_probs and len(transition_probs[phrase]) == 0:
            del transition_probs[phrase]
    return None


def prune_transitions(transition_probs: Dict[str, Dict[str, Dict[str, float]]], min_prob_threshold: float = 0.1,
                      from_phrase: bool = True, debug: bool = False) -> Dict[str, Dict[str, Dict[str, float]]]:
    for direction in transition_probs:
        if from_phrase:
            prune_phrase_transitions(transition_probs[direction], min_prob_threshold=min_prob_threshold, debug=debug)
        else:
            prune_word_transitions(transition_probs[direction], min_prob_threshold=min_prob_threshold, debug=debug)
        # print(len(transition_probs))
        following_nodes = get_nodes_following_phrase(transition_probs[direction], {'<PHRASE>'})
        start_nodes = list(transition_probs[direction].keys())
        for s in start_nodes:
            if s not in following_nodes:
                del transition_probs[direction][s]
    return transition_probs


def compute_transition_probs(phrases: Union[str, List[str]], context_count: Dict[str, Dict[str, Counter]],
                             min_prob_threshold: float = 0.1, min_word_prob: float = 0.1,
                             variant_of: Dict[str, str] = None,
                             from_phrase: bool = True,
                             debug: bool = False):
    if isinstance(phrases, str):
        phrases = [phrases]
    transition_freq = count_transitions(phrases, context_count, min_word_prob=min_word_prob,
                                        variant_of=variant_of, from_phrase=from_phrase)
    transition_probs = defaultdict(lambda: defaultdict(dict))
    for direction in transition_freq:
        for curr_node in transition_freq[direction]:
            total = sum(transition_freq[direction][curr_node].values())
            # print('curr_node:', curr_node)
            for next_node in transition_freq[direction][curr_node]:
                trans_freq = transition_freq[direction][curr_node][next_node]
                # print('next_node:', next_node)
                if from_phrase:
                    if isinstance(curr_node, tuple):
                        next_node = tuple(list(curr_node) + [next_node])
                    elif isinstance(next_node, tuple):
                        next_node = tuple([curr_node] + list(next_node))
                    else:
                        print('curr_node:', curr_node)
                        print('next_node:', next_node)
                        raise TypeError('when using from_phrase=True, curr_node or next_node must be a tuple')
                # print('next_node:', next_node)
                # print('\tfreq:', trans_freq, '\ttotal:', total)
                transition_probs[direction][curr_node][next_node] = trans_freq / total
    # print(len(transition_probs))
    transition_probs = prune_transitions(transition_probs, min_prob_threshold=min_prob_threshold,
                                         from_phrase=from_phrase, debug=debug)
    return transition_probs


def get_nodes_following_phrase(transition_probs, start_nodes: Set[str]):
    # print('start nodes:', start_nodes)
    following_nodes = copy.deepcopy(start_nodes)
    for curr_node in start_nodes:
        for next_node in transition_probs[curr_node]:
            if next_node not in following_nodes:
                # print('\tcurr_node:', curr_node, '\tadding', next_node)
                following_nodes.add(next_node)
                # print('\tnext node:', next_node)
                following_nodes = get_nodes_following_phrase(transition_probs, following_nodes)
    # print('returning nodes:', following_nodes)
    return following_nodes


def count_transitions(phrases: Union[str, List[str]], context_count: Dict[str, Dict[str, Counter]],
                      min_word_prob: float = 0.1, variant_of: Dict[str, str] = None,
                      from_phrase: bool = True) -> Dict[str, Dict[str, Counter]]:
    if variant_of is None:
        variant_of = {}
    transition_freq = {}
    for direction in {'pre', 'post'}:
        selected_words = select_context_words(phrases, context_count[direction], variant_of,
                                              min_word_prob=min_word_prob)
        # print('selected_words:', selected_words)
        selected_words.append('<PHRASE>')
        transition_freq[direction] = defaultdict(Counter)
        for phrase in phrases:
            for pc in context_count[direction][phrase]:
                norm_pc = normalise_context(pc.split(' '), variant_of)
                if direction == 'pre':
                    norm_pc = reversed(norm_pc)
                selected_pc = ['<PHRASE>'] + [w if w in selected_words else f'<VAR-{wi}>'
                                              for wi, w in enumerate(norm_pc)]
                for i in range(len(selected_pc)-1):
                    trans_word = selected_pc[i+1]
                    if from_phrase is True:
                        curr_phrase = tuple(selected_pc[:i+1])
                        # curr_word = selected_pc[i]
                        # print(f"{i: <4}{curr_word: <40}{trans_word: <20}\t{curr_phrase}")
                        transition_freq[direction][curr_phrase][trans_word] += context_count[direction][phrase][pc]
                    else:
                        curr_word = selected_pc[i]
                        transition_freq[direction][curr_word][trans_word] += context_count[direction][phrase][pc]
    return transition_freq
