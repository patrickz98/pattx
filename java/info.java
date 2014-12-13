import java.net.*;

public class info
{
	public static void main(String[] args) throws Exception
	{		
		InetAddress local = InetAddress.getLocalHost();
		String localhostname = local.getHostName();
        String ip = local.getCanonicalHostName();

		System.out.println("user:\t\t" + System.getProperty("user.name"));
		System.out.println("os:\t\t" + System.getProperty("os.name"));
		System.out.println("os version:\t" + System.getProperty("os.version"));
		System.out.println("system arch:\t" + System.getProperty("os.arch"));

		System.out.println("hostname:\t" + localhostname);
		System.out.println("local ip:\t" + ip);
		
		System.out.println("user dir:\t" + System.getProperty("user.dir"));
		System.out.println("java version:\t" + System.getProperty("java.version"));
		System.out.println("encoding:\t" + System.getProperty("sun.jnu.encoding"));

		System.out.println("file encoding:\t" + System.getProperty("file.encoding"));

// 		System.getProperties().list(System.out);
	}
}