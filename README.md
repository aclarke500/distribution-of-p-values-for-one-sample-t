# distribution-of-p-values-for-one-sample-t
<h1>Methods</h1>
<p>In Book1.csv, we have 50 random numbers between 1 and 100. </p>
<br><p>We import them into a Python script, and run a one-sample t-test on it repeatedly. We increment the predicted average, and can observe a normal distribution following the p-values. We can see the peak around 50ish as we would expect to be the average. This makes sense, seeing as a p-value in this case is simply the probability of a given number being the average. So as we tend further away from the average, the probability converges to 0.  </p>
<h2>The results: </h2>
<a href="https://ibb.co/p4n1sRd"><img src="https://i.ibb.co/nQRwVnj/Figure-1.png" alt="Figure-1" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'>upload</a><br />
<h3>True popultaion mean = 47.632653</h3>
<p>Here are the results. The red line is the true mean, 47.6. We can see that the p values move around that. If the data was truly meaned at 50, would you have p-value of 1.0? This is the question I hope to explore next.</p>