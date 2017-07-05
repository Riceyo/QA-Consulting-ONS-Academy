import java.sql.*;

public class DatabaseQuery
{
	public static void main(String args[])
	{
		try
		{
			Class.forName("com.mysql.jdbc.Driver");
			Connection con = DriverManager.getConnection ("jdbc:mysql://localhost:3306/blah","root", "password");  
			Statement stmt = con.createStatement();
			ResultSet rs = stmt.executeQuery ("SELECT * FROM BLAH");
			while (rs.next())
			{
				System.out.println(rs.getInt(1));
			}
		}
		catch(java.lang.Exception e)
		{
			System.out.println(e);
		}
	}
}
