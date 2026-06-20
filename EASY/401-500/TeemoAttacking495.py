class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # counter = 0
        # for i in range(0,len(timeSeries)-1):
        #     if abs(timeSeries[i] - timeSeries[i+1]) >= duration:
        #         counter += duration
        #     else:
        #         counter += duration - (abs(timeSeries[i] - timeSeries[i+1])) 
                                                
        # counter += duration

        # return counter

        counter = 0
        for i in range(0,len(timeSeries)-1):
            if abs(timeSeries[i] - timeSeries[i+1]) >= duration:
                counter += duration
            else:
                counter += abs(timeSeries[i] - timeSeries[i+1])
        counter += duration

        return counter