package com.example.locod.musicgenerator;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import java.lang.Process;
import java.lang.Runtime;


// TODO: reimplement musicgenerator in java
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private String cmd = "python3";
    private String path = "C:\\cygwin64\\home\\locod\\repos\\MusicGen";
    private String fileName = "musicgen.py";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Example of a call to a native method
        // TextView tv = (TextView) findViewById(R.id.sample_text);
        // tv.setText(stringFromJNI());
    }


    public void musicButton(View view) {
        CallMusicGenerator();
    }

    public void CallMusicGenerator() {
        try {
            Process p = Runtime.getRuntime().exec(cmd + " " + path);
            Log.d("button","Created music generator");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
