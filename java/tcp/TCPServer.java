import java.io.*;
import java.net.*;

public class TCPServer
{
	public static void main(String[] args) throws Exception
	{
		System.out.println("Server:");
		
		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("ip:\t" + ip);
		
		String clientSentence;
        String capitalizedSentence;
        ServerSocket welcomeSocket = new ServerSocket(6789);

        while(true)
        {
        	Socket connectionSocket = welcomeSocket.accept();
        	BufferedReader inFromClient =
               new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
        	DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
            clientSentence = inFromClient.readLine();
            System.out.println("Received: " + clientSentence);
            capitalizedSentence = clientSentence.toUpperCase() + "\n";
            outToClient.writeBytes(capitalizedSentence);
        }
	}
}