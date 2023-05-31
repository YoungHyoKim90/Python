package kr.co.aiai.app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView textView;
    private Button button;

    private int clickCount = 0;
    private String[] changeButton = {"Good Morning!", "Good Evening!", "Good Night!"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = findViewById(R.id.tv1);
        button = findViewById(R.id.btn1);

        TextView tv = findViewById(R.id.tv1);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickCount++;
                if(clickCount >= changeButton.length){
                    clickCount =0;
                }
                textView.setText(changeButton[clickCount]);
            }
        });

    }
}

