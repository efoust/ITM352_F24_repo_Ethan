
def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        print("On your way!")
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            print("Almost there!")
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
                    print("you win!")
    else:
        progress = "Get going!"

    return progress

def test_determine_progress(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
        assert progress_function(0,0), "Get going!" 
        assert progress_function(1,5), "On your way!"
        assert progress_function(4,10), "Almost there!"
        assert progress_function(6,10), "You Win!"


#def test_determine_progress1(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
    #    assert progress_function(10,0), "Get going!" 

#def test_determine_progress(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
   #     assert progress_function(5,10), "Get going!" 


test_determine_progress(determine_progress1)

#def determine_progress2(hits, spins):


