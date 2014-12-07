import java.io.*;
import java.net.*;
import javax.net.ssl.SSLServerSocket;
import javax.net.ssl.SSLServerSocketFactory;
import javax.net.ssl.SSLSocket;

public class SSLTCPServer
{
	public static void main(String[] arstring) throws Exception
	{
		System.out.println("Server:");
		
		String ip = Inet4Address.getLocalHost().getHostAddress();
		System.out.println("ip:\t" + ip);
		
		String clientSentence;
        String capitalizedSentence;
        
        SSLServerSocketFactory sslserversocketfactory =
                    (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();
        SSLServerSocket welcomeSocket = (SSLServerSocket) sslserversocketfactory.createServerSocket(7050);

        while(true)
        {
        	SSLSocket connectionSocket = (SSLSocket) welcomeSocket.accept();
        	
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