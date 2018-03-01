from hshbsh import Taxi

def writeJourneys(taxis):
    TOTAL_NUMBER_OF_TAXIS=1000
    TOTAL_NUMBER_OF_RIDES=10000
    outfilename="answer.txt"
    with open(outfilename,"w") as outfile:
        for i,taxi in enumerate(taxis):
            taxiID=i+1
            if taxiID < 1:
                raise TypeError("Error :: this taxi ID is {}, but it cannot be less than 1".format(taxiID))
            if taxiID > TOTAL_NUMBER_OF_TAXIS:
                raise TypeError("Error :: this taxi ID is {}, but there are only {} taxis available".format(taxiID,TOTAL_NUMBER_OF_TAXIS))
            numberOfJourneys=len(taxi)
            if numberOfJourneys < 0:
                raise TypeError("Error :: this taxis has {} rides assigned. It cannot be less than 0".format(numberOfJourneys))
            if numberOfJourneys > TOTAL_NUMBER_OF_RIDES:
                raise TypeError("Error :: this taxis has {} rides assigned but there are only {} rides available".format(numberOfJourneys,TOTAL_NUMBER_OF_RIDES))
            journeys=taxi.jids
            output=[taxiID,numberOfJourneys]+journeys
            output=[str(x) for x in output]
            outputString=" ".join(output)+"\n"
            print(outputString,end="")
            outfile.write(outputString)
    return

if __name__ == "__main__" : writeJourneys([[0,1,2],[3,4,5],[6,7,8,9,10]])
