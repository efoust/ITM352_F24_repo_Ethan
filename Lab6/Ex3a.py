def determine_progress2(hits,spins):
    if spins == 0:
        print("Get Going!")
        return "Get Going!"
    
    
    hits_spins_ratio = hits / spins

    progress = "Get Going!"

    if hits_spins_ratio > 0: 
        progress = "On your way!"
        print("On your way!")
    
    if hits_spins_ratio >= 0.25: 
        progress = "Almost there!"
        print("almost there!")
    
    if hits_spins_ratio >= 0.5 and hits < spins: 
        progress = "You Win!"
        print("you win!")


determine_progress2(10,0)

#def test_determine_progress2(progress_function):
 #   assert progress_function(1,0), "get Goin!"



#test_determine_progress2(determine_progress2)
#result = determine_progress2()
#print(result)