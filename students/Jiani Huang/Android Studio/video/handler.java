package com.example.video;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.icu.text.SimpleDateFormat;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class handler extends AppCompatActivity {
    private TextView textView;
    private Button stop,back_video,back_login;
    boolean flag = false;
    int time_a = 0;
    Handler handler = new Handler(){
        public void handleMessage(Message msg){
            if (msg.what == 0x01){
                textView.setText("计时器："+msg.obj.toString());
                //Toast.makeText(handler.this,"计时器：" +msg.obj.toString(),Toast.LENGTH_SHORT).show();
            }
            if (msg.what == 0x02){
                textView.setText("2222222");
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_handler);
        flag = true;
        textView = findViewById(R.id.textView);
        stop = findViewById(R.id.stop);
        back_video = findViewById(R.id.back_video);
        back_login = findViewById(R.id.back_login);
        new Thread(){
            public void run(){
                while (flag){
                    time_a = time_a+1;
                    SimpleDateFormat format = new SimpleDateFormat("yyyy年MM月dd HH:mm:ss");
                    String timeStr = format.format(System.currentTimeMillis());
                    Message msg = new Message();
                    msg.what = 0x01;
                    //msg.obj=timeStr;
                    msg.obj = time_a;
                    handler.sendMessage(msg);
                    try{
                        Thread.sleep(1000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }.start();
        stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag = false;
            }
        });
        back_video.setOnClickListener(new View.OnClickListener() {
            Intent intent_video = new Intent(handler.this, MainActivity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_video);
            }
        });
        back_login.setOnClickListener(new View.OnClickListener() {
            Intent intent_login = new Intent(handler.this, login.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_login);
            }
        });
    }
}
