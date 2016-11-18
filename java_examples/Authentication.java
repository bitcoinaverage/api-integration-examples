/*
 * Add reference to Gson Jar if you want to print nicely the received response. Otherwise you will need to delete the last lines in the Main.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

public class Authentication {

	static String getSignature(String secretKey, String publicKey) throws NoSuchAlgorithmException, InvalidKeyException {

		long timestamp = System.currentTimeMillis() / 1000L;
		String payload = timestamp + "." + publicKey;
		
		Mac sha256_Mac = Mac.getInstance("HmacSHA256");
		SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256");
		sha256_Mac.init(secretKeySpec);
		String hashHex = DatatypeConverter.printHexBinary(sha256_Mac.doFinal(payload.getBytes())).toLowerCase();
		String signature = payload + "." + hashHex;
		return signature;
	}
	
	public static void main(String[] args) throws IOException,
			NoSuchAlgorithmException, InvalidKeyException {
		String secretKey = "enter your secret key";
		String publicKey = "enter your public key";
		String signature = getSignature(secretKey, publicKey);
		
		String url = "https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD";
		URL urlObj = new URL(url);
		HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
		connection.setRequestMethod("GET");
		connection.setRequestProperty("X-Signature", signature);

		// read all the lines of the response into response StringBuffer
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
		String inputLine;
		StringBuffer response = new StringBuffer();

		while ((inputLine = bufferedReader.readLine()) != null) {
			response.append(inputLine);
		}
		bufferedReader.close();

		// if you don't want to use Gson, you can just print the plain response
		//System.out.println(response.toString());
		
		// print result in nice format using the Gson library
		Gson gson = new GsonBuilder().setPrettyPrinting().create();
		JsonParser jp = new JsonParser();
		JsonElement je = jp.parse(response.toString());
		String prettyJsonResponse = gson.toJson(je);
		System.out.println(prettyJsonResponse);
		
	}
}
