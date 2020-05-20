package com.example.new_test4;

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

public class Main2Activity extends AppCompatActivity {
    private Button button, button2;
    private TextView textView;
    boolean flag = false;
    int time_a = 0;
    Handler handler = new Handler(){
        public void handleMessage(Message msg){
            if(msg.what == 0x01){
                textView.setText("计时器:"+msg.obj.toString());
                Toast.makeText(Main2Activity.this,"计时器" + msg.obj.toString(),Toast.LENGTH_SHORT).show();
            }
            if(msg.what == 0x02){
                textView.setText("22222222");
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        flag = true;
        textView=findViewById(R.id.textView);
        button=findViewById(R.id.button);
        button2=findViewById(R.id.button2);
        new Thread(){
            public void run() {
                while (flag) {
                    time_a = time_a+1;
                    SimpleDateFormat format = new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss");
                    String timeStr = format.format(System.currentTimeMillis());
                    Message msg = new Message();
                    msg.what = 0x01;
                    msg.obj = timeStr;
                    //msg.obj = time_a;
                    handler.sendMessage(msg);
                    try {
                        Thread.sleep(2000);

                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }.start();
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag = false;
            }
        });
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Main2Activity.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}
