package com.example.logintovideo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;

public class Video extends AppCompatActivity {

    private Button btn_start,btn_end,button2,button3;
    private VideoView videoView;
    private MediaController mediaController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        initView();
    }
    private void initView(){
        videoView=(VideoView) findViewById(R.id.videoView);
        btn_start=(Button) findViewById(R.id.btn_start);
        btn_end=(Button) findViewById(R.id.byn_end);

        button2=(Button) findViewById(R.id.button2);
        button3=(Button) findViewById(R.id.button3);
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
        button3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent intent = new Intent(Video.this, Select.class);
                startActivity(intent);
            }
    });
    }
    private void init(){
        videoView=(VideoView) findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri ="android.resource://"+getPackageName()+"/"+R.raw.test1;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }
    private void init1(){
        videoView=(VideoView) findViewById(R.id.videoView);
        mediaController = new MediaController(this);
        String uri ="android.resource://"+getPackageName()+"/"+R.raw.test_mp3;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }
}
