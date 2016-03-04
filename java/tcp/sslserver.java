import java.io.*;
import java.net.*;
import javax.net.ssl.SSLServerSocket;
import javax.net.ssl.SSLServerSocketFactory;
import javax.net.ssl.SSLSocket;
import java.util.*;

public class sslserver
{
	public static void main(String[] arstring) throws Exception
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
