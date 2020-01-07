package com.example.pricetracker.Activities;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.example.pricetracker.R;
import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.components.AxisBase;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.formatter.IAxisValueFormatter;
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet;
import com.github.mikephil.charting.utils.ColorTemplate;
import com.jjoe64.graphview.DefaultLabelFormatter;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.io.DataOutput;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class ChartActivity extends AppCompatActivity {

    BarChart barChart;
    Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();

    @Override
    public void onBackPressed() {
        // TODO Auto-generated method stub
        super.onBackPressed();
        ChartActivity.this.overridePendingTransition(R.anim.splash_in,
                R.anim.splash_out);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chart);
        overridePendingTransition(R.anim.splash_in, R.anim.splash_out);
        setTitle("Statistics");
        map = (HashMap<String, ArrayList<String>>) getIntent().getSerializableExtra("chart");

        barChart = (BarChart) findViewById(R.id.barchart);

        barChart.setDrawBarShadow(false);
        barChart.setDrawValueAboveBar(true);
        barChart.setMaxVisibleValueCount(50);
        barChart.setPinchZoom(false);
        barChart.setDrawGridBackground(true);

        ArrayList<BarEntry> barEntries = new ArrayList<>();
    Iterator it = map.entrySet().iterator();
    int index = 1;
    String[] months = new String[100];

    while(it.hasNext()){

        Map.Entry pair = (Map.Entry)it.next();
        //Toast.makeText(getApplicationContext(),pair.getKey() + " " + pair.getValue(), Toast.LENGTH_LONG).show();
        barEntries.add(new BarEntry(index, Float.valueOf(pair.getValue().toString())));
        months[index] = pair.getKey().toString();
        index++;
    }


        /*barEntries.add(new BarEntry(1, 40f));
        barEntries.add(new BarEntry(2, 44f));
        barEntries.add(new BarEntry(3, 30f));
        barEntries.add(new BarEntry(4, 36f));*/

        ArrayList<BarEntry> barEntries1 = new ArrayList<>();

        barEntries1.add(new BarEntry(1, 0f));
        //barEntries1.add(new BarEntry(2, 54f));
        //barEntries1.add(new BarEntry(3, 60f));
        //barEntries1.add(new BarEntry(4, 31f));

        BarDataSet barDataSet = new BarDataSet(barEntries, "Date");
        barDataSet.setColors(ColorTemplate.COLORFUL_COLORS);

        BarDataSet barDataSet1 = new BarDataSet(barEntries1, "Price");
        barDataSet1.setColors(ColorTemplate.COLORFUL_COLORS);

        BarData data = new BarData(barDataSet, barDataSet1);

        float groupSpace = 0.1f;
        float barSpace = 0.02f;
        float barWidth = 0.43f;

        barChart.setData(data);

        data.setBarWidth(barWidth);
        barChart.groupBars(1, groupSpace, barSpace);




        XAxis xAxis = barChart.getXAxis();
        xAxis.setValueFormatter(new MyXAxisValueFormatter(months));
        xAxis.setPosition(XAxis.XAxisPosition.BOTH_SIDED);
        xAxis.setGranularity(1);
        xAxis.setCenterAxisLabels(true);
        xAxis.setLabelRotationAngle(60f);
        xAxis.setAxisMinimum(1);



    }

    public class MyXAxisValueFormatter implements IAxisValueFormatter{

        private String[] mValues;
        public MyXAxisValueFormatter(String[] values) {
            this.mValues = values;
        }

        @Override
        public String getFormattedValue(float value, AxisBase axis) {
            return mValues[(int)value];
        }
    }


}