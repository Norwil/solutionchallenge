public class Solution {
  public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
    
    int total = 0;
    for(int i = 0; i < classPoints.length; i++) {
      total = total + classPoints[i];
    }
    
    double average = total / classPoints.length;
    if(yourPoints > average){
      return true;
    }
    else{
      return false;
    }
  }
}