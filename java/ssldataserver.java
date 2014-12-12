import java.io.*;
import java.net.*;
import javax.net.ssl.*;
import java.util.*;

public class ssldataserver
{
	public static void main(String[] args) throws Exception
	{
		Properties systemProps = System.getProperties();
		systemProps.put( "javax.net.ssl.keyStore", "mySrvKeystore");
		systemProps.put( "javax.net.ssl.keyStorePassword", "123456");
		systemProps.put( "javax.net.ssl.trustStore", "mySrvKeystore");
		systemProps.put( "vax.net.ssl.trustStorePassword", "123456");
		System.setProperties(systemProps);

		System.out.println("Server:");
		
		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("ip:\t" + ip);

		int port = 7051;

 		ServerSocket serverSocket = null;

		try 
		{
		    SSLServerSocketFactory sslserversocketfactory =
                    (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
        	
        	serverSocket = sslserversocketfactory.createServerSocket(port);

// 			serverSocket = new ServerSocket(port);
		} 
		catch (IOException ex) 
		{
			System.out.println("Can't setup server on this port number. ");
		}

		SSLSocketFactory sslsocketfactory = (SSLSocketFactory) SSLSocketFactory.getDefault();

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