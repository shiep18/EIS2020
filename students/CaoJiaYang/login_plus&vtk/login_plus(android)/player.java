package com.example.two;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;

public class player extends AppCompatActivity {
    private VideoView videoView;
    private Button start,end,button4,button5;
    private MediaController mediaController;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_player);
        initView();
    }
    private void initView(){
        videoView=(VideoView)findViewById(R.id.videoView);
        start=(Button)findViewById(R.id.start);
        end=(Button)findViewById(R.id.end);
        button4=(Button)findViewById(R.id.button4);
        button5=(Button)findViewById(R.id.button5);
        start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                init();
            }
        });
        end.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                videoView.stopPlayback();
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                init1();
                //
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            Intent intent =new Intent(player.this, menu.class);
            @Override
            public void onClick(View v) {
                startActivity(intent);
            }
        });

    }
    private void init() {
        videoView=(VideoView)findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri="android.resource://"+getPackageName()+"/"+R.raw.control;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();

    }
    private void init1() {
        videoView=(VideoView)findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri="android.resource://"+getPackageName()+"/"+R.raw.voicebaidu;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();

    }
}
