package com.example.video;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Main3Activity extends AppCompatActivity {
    private Button video,time,back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        video=findViewById(R.id.video);
        time=findViewById(R.id.time);
        back=findViewById(R.id.back);
        video.setOnClickListener(new View.OnClickListener() {
            Intent intent_yp = new Intent(Main3Activity.this,Main2Activity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_yp);
            }
        });
        time.setOnClickListener(new View.OnClickListener() {
            Intent intent_jsq=new Intent(Main3Activity.this,Main4Activity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_jsq);
            }
        });
        back.setOnClickListener(new View.OnClickListener() {
            Intent intent_back=new Intent(Main3Activity.this,MainActivity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_back);
            }
        });
    }
}