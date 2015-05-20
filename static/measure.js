$(window).load(function() {
  if(!window.performance) {
    $("#result").innerText = "window.performance is undefind";
    return;
  }

  var resources = window.performance.getEntriesByType('resource');
  for(var k in resources) {
    var res = resources[k]
    if(res["initiatorType"] != "img") {
      continue;
    }

    process_measurement(res);
  }
});

function process_measurement(res) {
  var name = res["name"];
  var size = get_file_size(name);
  var dns_time = res["domainLookupEnd"] - res["domainLookupStart"];
  var tcp_time = res["connectEnd"] - res["connectStart"];
  var http_rt_time = res["responseEnd"] - res["requestStart"];
  var http_res_time = res["responseEnd"] - res["responseStart"];
  var speed = size * 1.0 / (http_res_time / 1000.0);

  dump(name, size, dns_time, tcp_time, http_rt_time, http_res_time, speed);
  post(name, size, dns_time, tcp_time, http_rt_time, http_res_time, speed);
};

function dump(name, size, dns_time, tcp_time, http_rt_time, http_res_time, speed) {
  add_message("file: " + name + " (size: " + size + " byte)");
  add_message('dns: ' + dns_time + ' ms')
  add_message('tcp: ' + tcp_time + ' ms')
  add_message('http(rtt): ' + http_rt_time + ' ms')
  add_message('http(res): ' + http_res_time + ' ms')
  add_message('speed: ' + speed + ' byte/sec')
};

function post(name, size, dns_time, tcp_time, http_rt_time, http_res_time, speed) {
  var data = {
    "name": name,
    "size": size,
    "dns_time": dns_time,
    "tcp_time": tcp_time,
    "http_rt_time": http_rt_time,
    "http_res_time": http_res_time
  };

  add_message("AJAXでデータ登録します")
  $.post("register", data, function(data){
    add_message("おわったにゃー");
  });
};

function add_message(msg) {
  $("#result").append('<p>' + msg + '</p>');
};

function get_file_size(path) {
  var sizes = {
    "neko.jpg": 31731,
    "inu.jpg": 193659
  };

  for(var k in sizes) {
    if(path.indexOf(k) >= 0) {
      return sizes[k];
    }
  }
  
  return 0;
};
