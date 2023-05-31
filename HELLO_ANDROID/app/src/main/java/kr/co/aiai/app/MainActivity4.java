package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Random;

public class MainActivity4 extends AppCompatActivity {

    private EditText et1, et2, et3 ;
    private Button btn ;
    private TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);

        et1 = findViewById(R.id.et1);
        et2 = findViewById(R.id.et2);
        btn = findViewById(R.id.btn1);
        tvResult = findViewById(R.id.tvResult);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int ran = new Random().nextInt(2)+1;

            String tvResult = (ran % 2 == 0) ? "짝" : "홀" ;

            et3.setText(tvResult);
            }
        });

    }
}


