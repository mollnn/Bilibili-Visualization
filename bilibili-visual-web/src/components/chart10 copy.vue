<template>
  <div style="width: 100%; height: 300px">
    <div id="echartContainer10" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
export default {
  name: "chart10",
  data() {
    return {};
  },
  methods: {
    draw() {
      var myChart = this.$echarts.init(
        document.getElementById("echartContainer10"),
        "infographic"
      );
      myChart.setOption({
    title: {
        text: '热点分析',
        link: 'https://www.baidu.com/s?wd=' + encodeURIComponent('ECharts'),
        x: 'center',
        textStyle: {
            fontSize: 23
        }

    },
    backgroundColor: '#FFFFFF',
    tooltip: {
        show: true
    },
    toolbox: {
        feature: {
            saveAsImage: {
                iconStyle: {
                    normal: {
                        color: '#FFFFFF'
                    }
                }
            }
        }
    },
    series: [{
        name: '热点分析',
        type: 'wordCloud',
        //size: ['9%', '99%'],
        sizeRange: [6, 66],
        //textRotation: [0, 45, 90, -45],
        rotationRange: [-45, 90],
        //shape: 'circle',
        textPadding: 0,
        autoSize: {
            enable: true,
            minSize: 6
        },
        textStyle: {
            normal: {
                color: function() {
                    return 'rgb(' + [
                        Math.round(Math.random() * 40 + 195),
                        Math.round(Math.random() * 50 + 145),
                        Math.round(Math.random() * 50 + 160)
                    ].join(',') + ')';
                }
            },
            emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
            }
        },
        data: [{name:"cnm", value:6666},{name:"fff", value:6666}]
    }]
});
      this.$http
        .get("http://131.mollnn.com:5000/api/v/danmu/wordcount/365972329/100/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          myChart.hideLoading();
          myChart.setOption({ series: [{ data: res.data }] });
          myChart.setOption({ series: [{ data:{name:"hhh", value:1} }] });
        });
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style></style>