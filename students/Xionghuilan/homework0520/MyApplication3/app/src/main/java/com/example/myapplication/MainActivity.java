package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;

public class MainActivity extends AppCompatActivity {
    private VideoView videoView;
    private Button btn_start,btn_end,button2,button3,button4;
    private MediaController mediaController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
    }

    private void initView() {
        videoView = findViewById(R.id.videoView);
        btn_start = findViewById(R.id.btn_start);
        btn_end = findViewById(R.id.btn_end);

        button2 = findViewById(R.id.button2);
        button3 = findViewById(R.id.button3);
        button4 = findViewById(R.id.button4);
        btn_start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                init();
            }
        });
        btn_end.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                videoView.stopPlayback();
            }
        });
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                init1();
            }
        });
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent_video = new Intent(MainActivity.this,Main2Activity.class);
                startActivity(intent_video);
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent_video = new Intent(MainActivity.this,Main3Activity.class);
                startActivity(intent_video);
            }
        });
    }

    private void init() {
        videoView = findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri = "android.resource://" + getPackageName() + "/" + R.raw.che;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }

    private void init1() {
        videoView = findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri = "android.resource://" + getPackageName() + "/" + R.raw.yinyue;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }
}
