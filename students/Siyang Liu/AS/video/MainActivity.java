package com.example.myvideo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;

public class MainActivity extends AppCompatActivity {
    private VideoView videoView;

    private Button btn_start,btn_end,button2,button3;
    private MediaController mediaController;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
    }

    private void initView(){
        videoView= (VideoView) findViewById(R.id.videoView);
        btn_start= (Button) findViewById(R.id.btn_start);
        btn_end= (Button) findViewById(R.id.btn_end);

        button2= (Button) findViewById(R.id.button2);
        button3= (Button) findViewById(R.id.button3);

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
            Intent intent_return = new Intent(MainActivity.this, Main3Activity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_return);
            }
        });


    }
    private void init(){
        videoView= (VideoView) findViewById(R.id.videoView);
        mediaController=  new MediaController(this);
        String uri= "android.resource://" + getPackageName() + "/" + R.raw.dkh;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }
    private void init1(){
        videoView= (VideoView) findViewById(R.id.videoView);
        mediaController= new MediaController(this);
        String uri= "android.resource://" + getPackageName() + "/" + R.raw.openingtitle;
        videoView.setVideoURI(Uri.parse(uri));
        videoView.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoView);
        videoView.requestFocus();
        videoView.start();
    }
}
