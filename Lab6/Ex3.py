def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress

def test_determine_progress(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
        assert progress_function(20,20), "Get going!" 


        

test_determine_progress(determine_progress1)

#def determine_progress2():
     