import java.io.*;
import java.net.*;
import javax.net.ssl.*;
import java.util.*;

class host extends Thread
{
	int host_port;
	
	host(int port)
	{
		host_port = port;
	}
	
	public void run()
	{
			try 
			{
				boolean con = false;
				String clientSentence;
				String capitalizedSentence;
		
				SSLServerSocketFactory sslserversocketfactory =
							(SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
		
				SSLServerSocket welcomeSocket = (SSLServerSocket) sslserversocketfactory.createServerSocket(host_port);

				while (isInterrupted() == false)
				{
					SSLSocket connectionSocket = (SSLSocket) welcomeSocket.accept();
					
					if (con == false)
					{
						System.out.print("new connection:\t");
						System.out.println(connectionSocket.getInetAddress());
						
						con = true;
					}
					
					BufferedReader inFromClient =
					   new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
					DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
					
					clientSentence = inFromClient.readLine();
					System.out.println("Received: " + clientSentence);
				}
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
			System.err.println("Connection closed");
			System.exit(0);
	}
}

class client extends Thread
{
	int host_port;
	String host_ip;
	
	client(int port, String hostip)
	{
		host_port = port;
		host_ip = hostip;
	}
	
	public void run()
	{
			try 
			{
				while (isInterrupted() == false) 
				{
					String sentence;
					String modifiedSentence;

					BufferedReader inFromUser = new BufferedReader( new InputStreamReader(System.in));
				
					SSLSocketFactory sslsocketfactory = (SSLSocketFactory) SSLSocketFactory.getDefault();
					SSLSocket clientSocket = (SSLSocket) sslsocketfactory.createSocket(host_ip, host_port);
					DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
	
					System.out.print("You: ");
 					sentence = inFromUser.readLine();
 					outToServer.writeBytes(sentence + '\n');
 							
					clientSocket.close();
				}
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
	}
}

class Chat
{
	public static void main(String[] args) throws Exception
	{
		System.out.println("configure system");
		
		Properties systemProps = System.getProperties();
		systemProps.put( "javax.net.ssl.keyStore", "mySrvKeystore");
		systemProps.put( "javax.net.ssl.keyStorePassword", "123456");
		systemProps.put( "javax.net.ssl.trustStore", "mySrvKeystore");
		systemProps.put( "vax.net.ssl.trustStorePassword", "123456");
		System.setProperties(systemProps);

		InetAddress local = InetAddress.getLocalHost();
		String localhostname = local.getHostName();
        String ip = local.getCanonicalHostName();

		int port = 7050;
		
		System.out.println("user:\t\t" + System.getProperty("user.name"));
		System.out.println("OS:\t\t" + System.getProperty("os.name"));
		System.out.println("system arch:\t" + System.getProperty("os.arch"));

		System.out.println("hostname:\t" + localhostname);
		System.out.println("local ip:\t" + ip);
		System.out.println("port:\t\t" + port);

// 		System.out.println("server is starting");
		host server = new host(port);
		server.start();
		
		System.out.print("host ip:\t");
		
		BufferedReader stdin = new BufferedReader( new InputStreamReader(System.in));
		String tmp = stdin.readLine();

		
// 		System.out.println("client is starting");
		client user = new client(port, tmp);
		user.start();
	}
}