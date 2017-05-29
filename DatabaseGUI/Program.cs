using System;
using System.IO;
using System.Collections.Generic;
using Gtk;

namespace DatabaseGUI
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Application.Init();
            Dictionary<string, string> settings = ReadSettings();
            Console.WriteLine(settings);
            MainWindow win = new MainWindow();
            win.Show();
            Application.Run();
        }

        static Dictionary<string, string> ReadSettings()
        {
            Dictionary<string, string> settings = new Dictionary<string, string>();
            using (var fs = File.OpenRead("Settings.txt"))
            using (var reader = new StreamReader(fs))
               while (!reader.EndOfStream) 
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');
                    settings.Add(values[0], values[1]);

                }
            return settings;
        }
    }
}
