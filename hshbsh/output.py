def create_output(taxis):
    TOTAL_NUMBER_OF_TAXIS=1000
    TOTAL_NUMBER_OF_RIDES=10000
    outputString=""
    for i,taxi in enumerate(taxis):
        taxiID=i+1
        if taxiID < 1:
            raise TypeError("Error :: this taxi ID is {}, but it cannot be less than 1".format(taxiID))
        if taxiID > TOTAL_NUMBER_OF_TAXIS:
            raise TypeError("Error :: this taxi ID is {}, but there are only {} taxis available".format(taxiID,TOTAL_NUMBER_OF_TAXIS))
        journeys=taxi.jids
        numberOfJourneys=len(journeys)
        if numberOfJourneys < 0:
            raise TypeError("Error :: this taxis has {} rides assigned. It cannot be less than 0".format(numberOfJourneys))
        if numberOfJourneys > TOTAL_NUMBER_OF_RIDES:
            raise TypeError("Error :: this taxis has {} rides assigned but there are only {} rides available".format(numberOfJourneys,TOTAL_NUMBER_OF_RIDES))
        output=[numberOfJourneys]+journeys
        output=[str(x) for x in output]
        outputString+=" ".join(output)+"\n"
    return outputString



def write_journeys(taxis,outfilename="answer.txt",writeToFile=True):
    if writeToFile:
        with open(outfilename,"w") as outfile:
            outputString=create_output(taxis)
            outfile.write(outputString)
    else:
        outputString=create_output(taxis)
        return outputString

if __name__ == "__main__" : write_journeys([[0,1,2],[3,4,5],[6,7,8,9,10]],"answer.txt",False)
