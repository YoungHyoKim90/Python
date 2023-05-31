package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Random;

public class MainActivity6 extends AppCompatActivity {

    private TextView tv1;
    private TextView tv2;
    private TextView tv3;
    private TextView tv4;
    private TextView tv5;
    private TextView tv6;
    private Button btn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main6);

        TextView tv1 = findViewById(R.id.tv1);
        TextView tv2 = findViewById(R.id.tv2);
        TextView tv3 = findViewById(R.id.tv3);
        TextView tv4 = findViewById(R.id.tv4);
        TextView tv5 = findViewById(R.id.tv5);
        TextView tv6 = findViewById(R.id.tv6);
        Button btn = findViewById(R.id.btn1);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View vt1) {
                int lotto[] = new int[6];
                Random random = new Random();

                for (int i = 0; i < lotto.length; i++) {
                    int num;
                    boolean duplicate;

                    do {
                        num = random.nextInt(45) + 1;
                        duplicate = false;

                        for (int j = 0; j < i; j++) {
                            if (lotto[j] == num) {
                                duplicate = true;
                                break;
                            }
                        }
                    } while (duplicate);

                    lotto[i] = num;
                }

                tv1.setText(String.valueOf("          " + lotto[0] + "    "));
                tv2.setText(String.valueOf(lotto[1] + "    "));
                tv3.setText(String.valueOf(lotto[2] + "    "));
                tv4.setText(String.valueOf(lotto[3] + "    "));
                tv5.setText(String.valueOf(lotto[4] + "    "));
                tv6.setText(String.valueOf(lotto[5] + "    "));
            }
        });


    }
}


