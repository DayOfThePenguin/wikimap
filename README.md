<h1>WIKIMAP</h1>
<h4>A python web application to map the connectivity of wikipedia pages</h4>
<h2>Setup steps:</h2>

<ol>
     <li>
          <h4>Clone this repository</h4>
          <ul>
               <li><code>git clone https://github.com/DayOfThePenguin/wikimap.git</code></li>
          </ul>
     </li>
     <li>
          <h4>Install <a href="https://virtualenv.pypa.io/en/latest/">Virtualenv</a> and create a new environment</h4>
          <ul>
               <li><code>virtualenv env</code></li>
               <em>NOTE: The `.gitignore` file for this repository assumes that you call your virtual environment `env`.  You can change this behavior by editing the `.gitignore` file and adding the name you chose for your environment.</em>
          </ul>
     </li>
     <li>
          <h4>Activate your new environment and install Wikimap's dependencies</h4>
          <em>NOTE: the following assumes (1) that you created your Virtualenv in the same directory that you cloned this repository into and (2) you are currently in that directory.  Modify according to your set-up.</em>
         
          <h5>Activate the environment</h5>
          <ul>
               <li>BASH: <code>source env/bin/activate</code></li>
               <li>CSH: <code>source env/bin/activate.csh</code></li>
          </ul>
          <h5>Install our dependencies</h5>
          <ul>
               <li><code>pip install flask</code> : <a href="http://flask.pocoo.org/">Flask</a> is the library we use for web back-end things that are hard to do by hand</li>
               <li><code>pip install python-igraph</code> : <a href="http://igraph.org/python/">Igraph</a> is the library we use to do graph operations that would be really hard to do with lists or other standard Python objects</li>
               <li><code>pip install pycapnp</code> : <a href="http://jparyani.github.io/pycapnp/index.html">Pycapnp</a>, a Python implementation of <a href="https://capnproto.org/index.html">Cap’n Proto</a> serialization data interchange format, which we use for data wrangling.</li>
     </li>
</ol>

<h2>Success!  You can now run the 'wikimap.py' script in the root directory of this repository</h2>
<code>python wikimap.py<code>
<em>NOTE: If you have any problems, open an issue and we'll do our best to help you out!</em>
     
