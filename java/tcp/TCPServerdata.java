import java.io.*;
import java.net.*;

public class TCPServerdata
{
	public static void main(String[] args) throws Exception
	{
		System.out.println("Server:");
		
		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("ip:\t" + ip);

		ServerSocket serverSocket = null;

		try 
		{
			serverSocket = new ServerSocket(4444);
		} 
		catch (IOException ex) 
		{
			System.out.println("Can't setup server on this port number. ");
		}

		Socket socket = null;
		InputStream is = null;
		FileOutputStream fos = null;
		BufferedOutputStream bos = null;
		int bufferSize = 0;

		try 
		{
			socket = serverSocket.accept();
		} 
		catch (IOException ex) 
		{
			System.out.println("Can't accept client connection. ");
		}

		try 
		{
			is = socket.getInputStream();

			bufferSize = socket.getReceiveBufferSize();
			System.out.println("Buffer size: " + bufferSize);
		} 
		catch (IOException ex) 
		{
			System.out.println("Can't get socket input stream. ");
		}

		try 
		{
			fos = new FileOutputStream("test.jpg");
			bos = new BufferedOutputStream(fos);

		} 
		catch (FileNotFoundException ex) 
		{
			System.out.println("File not found. ");
		}

		byte[] bytes = new byte[bufferSize];

		int count;

		while ((count = is.read(bytes)) > 0) 
		{
			bos.write(bytes, 0, count);
		}

		bos.flush();
		bos.close();
		is.close();
		socket.close();
		serverSocket.close();
	}
}