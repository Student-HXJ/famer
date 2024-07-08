using System;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class MyClient : MonoBehaviour
{
    private TcpClient socketConnection;
    private NetworkStream stream;

    public static MyClient Instance {get; set;}

    private void Awake()
    {
        Instance = this;
    }

    void Start()
    {
        ConnectToServer();
    }

    void ConnectToServer()
    {
        try
        {
            socketConnection = new TcpClient("127.0.0.1", 8080);
            stream = socketConnection.GetStream();
            Debug.Log("Connected to server.");
        }
        catch (Exception e)
        {
            Debug.Log("Socket error: " + e);
        }
    }

    void Update()
    {
    }

    public void SendMessageToServer(string message)
    {
        if (socketConnection == null) return;

        try
        {
            byte[] data = Encoding.UTF8.GetBytes(message);
            stream.Write(data, 0, data.Length);
            stream.Flush();  // 确保数据被发送

            // Receive a response from the server
            // data = new byte[1024];
            // int bytesRead = stream.Read(data, 0, data.Length);
            // string response = Encoding.UTF8.GetString(data, 0, bytesRead);
            // Debug.Log(response);
        }
        catch (Exception e)
        {
            Debug.Log("Error sending message: " + e);
        }
    }

    void OnApplicationQuit()
    {
        if (stream != null) stream.Close();
        if (socketConnection != null) socketConnection.Close();
    }
}