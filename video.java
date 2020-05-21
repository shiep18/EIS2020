package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;

public class video extends AppCompatActivity {
    private VideoView videoView;
    private Button btn_start,btn_end,button3,button4;
    private MediaController mediaController;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_video);
        initView();
    }

    private  void initView(){
        videoView = (VideoView) findViewById(R.id.videoView);
        btn_start = (Button) findViewById(R.id.btn_start);
        btn_end = (Button) findViewById(R.id.btn_end);
        button3 = (Button) findViewById(R.id.button3);
        button4 = (Button) findViewById(R.id.button4);
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
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                init1();
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(video.this,Main2Activity.class);
                startActivity(intent);
            }
        });

    }

    private void init(){
        videoView = (VideoView) findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri = "android.resource://"+getPackageName()+"/"+R.raw.attitude;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }

    private void init1(){
        videoView = (VideoView) findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri = "android.resource://"+getPackageName()+"/"+R.raw.how;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }
}
