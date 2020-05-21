package com.example.myvideo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;

public class Main4Activity extends AppCompatActivity {
    private Button back2, stop;
    private TextView textView;

    boolean flag= false;
    int time_a= 0;
    Handler handler = new Handler(){
        public void handleMessage(Message msg){
            if (msg.what == 0x01){
                textView.setText("计时器： " + msg.obj.toString());
                Toast.makeText(Main4Activity.this,"计时器："+msg.obj.toString(),Toast.LENGTH_SHORT).show();
            }
            if (msg.what == 0x02){
                textView.setText("233333333");
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);
        flag = true;
        textView = findViewById(R.id.textView4);
        stop = findViewById(R.id.Stop);
        back2 = findViewById(R.id.Back2);
        back2.setOnClickListener(new View.OnClickListener() {
            Intent intent_back = new Intent(Main4Activity.this, Main3Activity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_back);
            }
        });
        new Thread(){
            public void run(){
                while (flag){
                    time_a = time_a+1;
                    SimpleDateFormat format = new SimpleDateFormat("yyyy年MM月dd HH：mm：ss");
                    String timeStr = format.format(System.currentTimeMillis());
                    Message msg = new Message();
                    msg.what = 0x01;
                    msg.obj = time_a;
                    handler.sendMessage(msg);
                    try{
                        Thread.sleep(2000);
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
    }
}