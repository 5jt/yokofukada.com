<html>
<head>
<script type="text/javascript">
<!--
popWidth = Math.min(800,screen.availWidth)
popHeight = Math.min(700,screen.availHeight)
popX = Math.round((screen.availWidth - popWidth)/2)
popY = Math.round((screen.availHeight - popHeight)/2)
window.resizeTo(popWidth,popHeight)
window.moveTo(popX,popY)
//-->
</script>

<style>
	body {	background:rgb(196,196,196);}
	p { font-family:Gill Sans MT,Arial,Helvetica,swiss,sans-serif;
		font-size:100%;
		margin:0px;}
	div{margin-top:40px;text-align:center;}
	img{border:1px solid #aaa;margin:20px;}
	a {text-decoration:none}
	a:hover {text-decoration:underline}
</style>

<title>Jewellery | Yoko Fukada</title>
</head>


<body><div>
<img src='images/Untitled-<? echo $_GET['pic']; ?>.jpg' alt='Jewellery by Yoko Fukada' title='Jewellery by Yoko Fukada' />
</div>

<p style='position:absolute;left:10px;top:10px'>&laquo;<a href='jw.php?pic=<?echo 1+($_GET['pic']+10)%12; ?>'>prev</a></p>
<p style='position:absolute;right:10px;top:10px'><a href='jw.php?pic=<? echo 1+$_GET['pic']%12; ?>'>next</a>&raquo;</p>

<p style='font-size:60%;color:blue;position:absolute; bottom:5px; right:5px;'>Photography by: 
<a href="http://homepage1.nifty.com/nomurasa/1f-c.htm" title="Photography by Sadanori Nomura">Sadanori Nomura</a></p>

<p style='position:absolute;left:50%;top:10px' onclick='window.close()'><a href='jw.php'>back</a></p>
</body>
</html>