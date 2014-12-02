import java.io.*;
import java.net.*;

class TCPdata
{
	public static void main(String argv[]) throws Exception
	{
		System.out.println("Client:");

		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("ip:\t" + ip);
		
		Socket socket = null;
		String host = "127.0.0.1";

		socket = new Socket(host, 4444);

		File file = new File("mandrill.jpg");
		// Get the size of the file
		
		long length = file.length();
		if (length > Integer.MAX_VALUE) 
		{
			System.out.println("File is too large.");
		}
		
		byte[] bytes = new byte[(int) length];
		FileInputStream fis = new FileInputStream(file);
		BufferedInputStream bis = new BufferedInputStream(fis);
		BufferedOutputStream out = new BufferedOutputStream(socket.getOutputStream());

		int count;

		while ((count = bis.read(bytes)) > 0) 
		{
			out.write(bytes, 0, count);
		}

		out.flush();
		out.close();
		fis.close();
		bis.close();
		socket.close();
	}
}