using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using UnityEngine.UI;

public class test : MonoBehaviour
{
    public InputField positionsInput;
    public InputField durationInput;
    public InputField timeStampInput;
    public Button addButton;
    public Button delButton;
    public Button resetButton;
    public Button runButton;
    public Task task;
    public List<Task> tasks;
    public List<Position> positions;
    public Mission mission;

    [Serializable]
    public class Mission
    {
        public List<Task> tasks;
        public Mission()
        {
            tasks = new List<Task>();
        }
    }

    [Serializable]
    public class Position
    {
        public int x = 0;
        public int y = 0;
    }

    [Serializable]
    public class Task
    {
        public float duration = 0.5f;
        public int timeStamp = 0;
        public List<Position> positions;

        public Task()
        {
            positions = new List<Position>();
        }

        public void Clear()
        {
            positions.Clear();
            duration = 0;
            timeStamp = 0;
        }

        public Task Clone()
        {
            Task newTask = new Task();
            newTask.duration = this.duration;
            newTask.timeStamp = this.timeStamp;
            foreach (var pos in this.positions)
            {
                newTask.positions.Add(new Position { x = pos.x, y = pos.y });
            }
            return newTask;
        }
    }

    // Start is called before the first frame update
    void Start()
    {   
        mission = new Mission();
        task = new Task();
        tasks = new List<Task>();
        positions = new List<Position>();
        positionsInput.onEndEdit.AddListener(OnPositionsEndEdit);
        durationInput.onEndEdit.AddListener(OnDurationEndEdit);
        timeStampInput.onEndEdit.AddListener(OnTimeStampEndEdit);
        if (addButton != null && delButton != null && resetButton != null)
        {
            addButton.onClick.AddListener(OnAddButtonClick);
            delButton.onClick.AddListener(OnDelButtonClick);
            resetButton.onClick.AddListener(OnResetButtonClick);
            runButton.onClick.AddListener(OnRunButtonClick);
        }
    }

    void OnPositionsEndEdit(string input)
    {
        if (input == null)
        {
            return;
        }
        positions.Clear();
        string[] positionsPairs = input.Split(';');
        foreach (string pair in positionsPairs)
        {
            string[] coordinates = pair.Split(',');
            if (coordinates.Length == 2)
            {
                if (int.TryParse(coordinates[0], out int x) && int.TryParse(coordinates[1], out int y))
                {
                    positions.Add(new Position { x = x, y = y });
                }
            }
        }
        task.positions = positions;
    }

    void OnDurationEndEdit(string input)
    {
        if (float.TryParse(input, out float duration))
        {
            task.duration = duration;
        }
    }

    void OnTimeStampEndEdit(string input)
    {
        if (int.TryParse(input, out int timeStamp))
        {
            task.timeStamp = timeStamp;
        }
    }

    void OnRunButtonClick()
    {
        mission.tasks = tasks;
        MyClient.Instance.SendMessageToServer(JsonUtility.ToJson(mission));
    }

    void OnDelButtonClick()
    {
        int cnt = tasks.Count;
        if (cnt > 0)
        {
            tasks.RemoveAt(cnt - 1);
        }
    }

    void OnResetButtonClick()
    {
        tasks.Clear();
    }

    void OnAddButtonClick()
    {
        if (task.positions.Count == 0)
        {
            return;
        }
        Debug.Log("add one task");
        tasks.Add(task.Clone());

        positionsInput.text = "";
        durationInput.text = "";
        timeStampInput.text = "";
        task.Clear();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Q))
        {
            MyClient.Instance.SendMessageToServer("q");
        }
    }
}
