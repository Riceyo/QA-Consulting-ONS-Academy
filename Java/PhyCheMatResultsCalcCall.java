
public class PhyCheMatResultsCalcCall {
	
	public static void main(String args[]) {
		PhyCheMatResultsCalc peter, luke;
		peter = new PhyCheMatResultsCalc();
		peter.phy=75;
		peter.che=80;
		peter.mat=90;
		peter.calc();
		peter.display();
		luke = new PhyCheMatResultsCalc();
		luke.phy = 100;
		luke.che = 100;
		luke.mat = 100;
		luke.calc();
		luke.display();		
	}
}
