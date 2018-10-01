C++
====

1. Convert between byte string to wide char


```
    std::wstring_convert<std::codecvt_utf8<wchar_t>> cvt;
    std::wstring out = cvt.from_bytes(fmt.str());
```

2. boost::format

```
    boost::format fmt = boost::format("CL Error: %d\n%s\n") % *err % boost::diagnostic_information(e);
    std::cerr << fmt.str() << std::endl;
```

3. format datetime using boost

```
    boost::posix_time::wtime_facet *facet = new boost::posix_time::wtime_facet(_T("%Y%m%d_%H%M%S"));

	boost::posix_time::ptime local_time = boost::posix_time::second_clock::local_time();

	std::wstringstream ss;
	ss.imbue(std::locale(std::locale::classic(), facet));

	//boost::local_time::local_date_time ldt = boost::local_time::local_sec_clock::local_time();
	ss << local_time;

	boost::wformat output_file_format = boost::wformat(_T("%s_%s.%s"));
```