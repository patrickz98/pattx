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
				String clientSentence;
				String capitalizedSentence;
		
				SSLServerSocketFactory sslserversocketfactory =
							(SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
		
				SSLServerSocket welcomeSocket = (SSLServerSocket) sslserversocketfactory.createServerSocket(host_port);

				while(isInterrupted() == false)
				{
					SSLSocket connectionSocket = (SSLSocket) welcomeSocket.accept();
			
					BufferedReader inFromClient =
					   new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
					DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
					
					clientSentence = inFromClient.readLine();
					System.out.println("Received: " + clientSentence);

		//             capitalizedSentence = clientSentence.toUpperCase() + "\n";
		//             outToClient.writeBytes(capitalizedSentence);
				}
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
			System.err.println("ende");
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
	
// 					BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
					System.out.print("You: ");
 					sentence = inFromUser.readLine();
 					outToServer.writeBytes(sentence + '\n');
// 					modifiedSentence = inFromServer.readLine();
// 					System.out.println("FROM SERVER: " + modifiedSentence);
		
					clientSocket.close();
				}
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
	}
}

public class Chat
{
	public static void main(String[] arstring) throws Exception
	{
		int port = 7050;

		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("port:\t\t" + port);
		System.out.println("local ip:\t" + ip);
		
		System.out.println("host is starting");
		host server = new host(port);
		server.start();
		
		System.out.print("Host ip:\t");
		BufferedReader stdin = new BufferedReader( new InputStreamReader(System.in));
		String tmp = stdin.readLine();

		
		System.out.println("client is starting");
		client user = new client(port, tmp);
		user.start();
	}
}