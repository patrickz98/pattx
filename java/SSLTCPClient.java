import java.io.*;
import java.net.*;
import javax.net.ssl.*;

class SSLTCPClient
{
	public static void main(String argv[]) throws Exception
	{
		System.out.println("Client:");

		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("ip:\t" + ip);

		try 
		{
			while (true) 
			{
				String sentence;
				String modifiedSentence;

				BufferedReader inFromUser = new BufferedReader( new InputStreamReader(System.in));
				
				SSLSocketFactory sslsocketfactory = (SSLSocketFactory) SSLSocketFactory.getDefault();
				SSLSocket clientSocket = (SSLSocket) sslsocketfactory.createSocket("localhost", 7050);
				DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
	
				BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		
				sentence = inFromUser.readLine();
				outToServer.writeBytes(sentence + '\n');
				modifiedSentence = inFromServer.readLine();
				System.out.println("FROM SERVER: " + modifiedSentence);
		
				clientSocket.close();
			}
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}