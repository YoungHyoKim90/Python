package kr.co.aiai.app;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity3 extends AppCompatActivity {

    private EditText et1, et2, et3;
    private Button button;
    private TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        et1 = findViewById(R.id.et1);
        et2 = findViewById(R.id.et2);
        et3 = findViewById(R.id.et3);
        button = findViewById(R.id.button2);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateSum();
            }
        });
    }

    private void calculateSum() {
        String value1 = et1.getText().toString();
        String value2 = et2.getText().toString();
        Log.d("YoungHyo90",value1);

        if (!value1.isEmpty() && !value2.isEmpty()) {
            int num1 = Integer.parseInt(value1);
            int num2 = Integer.parseInt(value2);
            int sum = num1 + num2;
            et3.setText(String.valueOf(sum));
        } else {
            et3.setText("입력해주세요.");
        }
    }
}


