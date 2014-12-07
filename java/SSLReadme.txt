keytool -genkey -keystore mySrvKeystore -keyalg RSA

java -Djavax.net.ssl.keyStore=mySrvKeystore -Djavax.net.ssl.keyStorePassword=123456 SSLTCPServer

java -Djavax.net.ssl.trustStore=mySrvKeystore -Dvax.net.ssl.trustStorePassword=123456 SSLTCPClient

java -Djavax.net.ssl.keyStore=mySrvKeystore -Djavax.net.ssl.keyStorePassword=123456 -Djavax.net.ssl.trustStore=mySrvKeystore -Dvax.net.ssl.trustStorePassword=123456 Chat