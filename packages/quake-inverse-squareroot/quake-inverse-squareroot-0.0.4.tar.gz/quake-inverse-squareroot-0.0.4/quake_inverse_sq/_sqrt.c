/*
Source from https://en.wikipedia.org/wiki/Fast_coarse_inv_sqrt
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>

static PyObject *coarse_inv_sqrt(PyObject *self, PyObject *args)
{
	const float number;
	long i;
	float x2, y;
	const float threehalfs = 1.5F;
	const what_the_fuck = 0x5f3759df;

	if (!PyArg_ParseTuple(args, "f", &number)) return NULL;
	if (number == 0){
		PyErr_SetString(PyExc_ZeroDivisionError, "division by zero");
		return NULL;
	}
	
	if (number < 0){
		PyErr_SetString(PyExc_ValueError, "Negative number");
		return NULL;
	}

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // evil floating point bit level hacking
	i  = what_the_fuck - ( i >> 1 );               // what the fuck? 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

	return Py_BuildValue("f", y);
}

static PyObject *fined_inv_sqrt(PyObject *self, PyObject *args){
	const float number;

	if (!PyArg_ParseTuple(args, "f", &number)) return NULL;
	if (number == 0){
		PyErr_SetString(PyExc_ZeroDivisionError, "division by zero");
		return NULL;
	}
	if (number < 0){
		PyErr_SetString(PyExc_ValueError, "Negative number");
		return NULL;
	}

	return Py_BuildValue("f", 1 / sqrt(number));
}

static PyMethodDef methods[] = {
	{"coarse_inv_sqrt", coarse_inv_sqrt, METH_VARARGS, "Coarse inverse square root. (Implementation from Wikipedia)"},
	{"fined_inv_sqrt", fined_inv_sqrt, METH_VARARGS, "Fined inverse square root. (Implementation from math.h)"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"quake_inverse_sq._sqrt",
	"Inverse square root implementations. (Implementation from Wikipedia and math.h)",
	-1,
	methods
};

PyMODINIT_FUNC PyInit__sqrt(void)
{
	PyObject *logging = PyImport_ImportModule("logging");
	PyObject *logger = PyObject_CallMethod(logging, "getLogger", "s", "quake_inverse_sq._sqrt_c");
	PyObject *logger_debug = PyObject_GetAttrString(logger, "debug");
	PyObject_CallFunctionObjArgs(logger_debug, PyUnicode_FromString("Loaded a module extension. Enjoy fast speed!"), NULL);
	Py_DECREF(logger_debug);// Imagine dropping
	Py_DECREF(logger);      // All of this
	Py_DECREF(logging);     // For "Memory Safety"
	return PyModule_Create(&module);
}

