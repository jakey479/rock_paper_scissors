def winner_is(p1_results, p2_results):
    if any([p1_results == 'rock' and p2_results == 'scissors',
            p1_results == 'paper' and p2_results == 'rock',
            p1_results == 'scissors' and p2_results == 'paper']):
        return 'p1'
    if any([p2_results == 'rock' and p1_results == 'scissors',
            p2_results == 'paper' and p1_results == 'rock',
            p2_results == 'scissors' and p1_results == 'paper']):
        return 'p2'
    if any([p2_results == 'rock' and p1_results == 'rock',
            p2_results == 'scissors' and p1_results == 'scissors',
            p2_results == 'paper' and p1_results == 'paper']):
        return 'none'
