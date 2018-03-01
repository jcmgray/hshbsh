from hshbsh import Taxi

def writeJournies(taxis):
    outfilename="answer.txt"
    with open(outfilename,"w") as outfile:
        for i,taxi in enumerate(taxis):
            taxiID=i+1
            numberOfJourneys=len(taxi)
            journeys=taxi
            output=[taxiID,numberOfJourneys]+journeys
            output=[str(x) for x in output]
            outputString=" ".join(output)+"\n"
            print(outputString,end="")
            outfile.write(outputString)
    return

if __name__ == "__main__" : writeJournies([[0,1,2],[3,4,5],[6,7,8,9,10]])
