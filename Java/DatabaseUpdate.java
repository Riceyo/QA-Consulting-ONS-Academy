import java.sql.*;

public class DatabaseUpdate
{
	public static void main(String args[])
	{
		try
		{
			Class.forName("com.mysql.jdbc.Driver");
			Connection con = DriverManager.getConnection ("jdbc:mysql://localhost:3306/blah","root", "password");  
			Statement stmt = con.createStatement();
			stmt.executeUpdate("insert into blah values(5)");
		}
		catch(java.lang.Exception e)
		{
			System.out.println(e);
		}

	}
}

