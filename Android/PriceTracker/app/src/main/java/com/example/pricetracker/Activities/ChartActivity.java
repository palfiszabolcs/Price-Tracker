package com.example.pricetracker.Activities;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import com.example.pricetracker.R;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet;
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
import java.util.Map;

public class ChartActivity extends AppCompatActivity {

    private GraphView graphview;
    LineGraphSeries<DataPoint> series;
    private LineChart mChart;
    SimpleDateFormat format = new SimpleDateFormat("mm:ss");
    Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chart);
        setTitle("Statistics");
        //graphview = findViewById(R.id.lineChart);
        mChart = findViewById(R.id.lineChart);
        map = (HashMap<String, ArrayList<String>>) getIntent().getSerializableExtra("chart");
        createChart();

    }

    private DataPoint[] getDataPoint(){
        DataPoint[] dp = new DataPoint[]{
                new DataPoint(new Date().getTime(), 1),
                new DataPoint(new Date().getTime(), 2),
                new DataPoint(new Date().getTime(), 3),
                new DataPoint(new Date().getTime(), 4),
                new DataPoint(new Date().getTime(), 5),
                new DataPoint(new Date().getTime(), 6),
                new DataPoint(new Date().getTime(), 75),
                new DataPoint(new Date().getTime(), 1342),
                new DataPoint(new Date().getTime(), 34),
                new DataPoint(new Date().getTime(), 65),
                new DataPoint(new Date().getTime(), 9)
        };
        return dp;
    }

    void createChart(){
        mChart.setDragEnabled(true);
        mChart.setScaleEnabled(false);
        ArrayList<Entry> values = new ArrayList<>();
        values.add(new Entry(5, 60f));
        values.add(new Entry(8, 50f));
        values.add(new Entry(12, 70f));
        values.add(new Entry(new Date().getTime(), 30f));
        values.add(new Entry(new Date().getTime(), 50f));
        values.add(new Entry(new Date().getTime(), 60f));
        values.add(new Entry(new Date().getTime(), 65f));

        LineDataSet set1 = new LineDataSet(values, "Shopping");
        set1.setFillAlpha(110);

        ArrayList<ILineDataSet> dataSets = new ArrayList<>();
        dataSets.add(set1);
        LineData data = new LineData(dataSets);
        mChart.setData(data);


    }

}