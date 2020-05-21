package com.example.logintovideo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Select extends AppCompatActivity {
    private Button Player,Timer,Exit;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select);

        Player=findViewById(R.id.Player);
        Player.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent intent = new Intent(Select.this,Video.class);
                startActivity(intent);
            }
        });
        Timer=findViewById(R.id.Timer);
        Timer.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent intent = new Intent(Select.this,Timer.class);
                startActivity(intent);
            }
        });

        Exit=findViewById(R.id.Exit);
        Exit.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent intent = new Intent(Select.this,Login.class);
                startActivity(intent);
            }
        });
    }
}
