# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xarray_ome_ngff', 'xarray_ome_ngff.v05']

package_data = \
{'': ['*']}

install_requires = \
['pint>=0.20.1,<0.21.0',
 'pydantic-ome-ngff>=0.1.3,<0.2.0',
 'pydantic>=1.10.4,<2.0.0',
 'xarray>=2023.2.0,<2024.0.0']

setup_kwargs = {
    'name': 'xarray-ome-ngff',
    'version': '1.1.0',
    'description': 'xarray and ome-ngff',
    'long_description': '# xarray-ome-ngff\nIntegration between xarray and the ome-ngff data model.\n\nAt present (February, 2023) this is a partial implementation of the [OME-NGFF spec](https://ngff.openmicroscopy.org/latest/#implementations). Specifcally, *only* the [`multiscales`](https://ngff.openmicroscopy.org/latest/#multiscale-md) and specs required by `multiscales` are implemented. Complete support for the spec would be welcome.\n\n## How it works\nThis library depends on [`pydantic-ome-ngff`](https://github.com/JaneliaSciComp/pydantic-ome-ngff) which implements OME-NGFF metadata as [pydantic](https://docs.pydantic.dev/) models. \n[`Axes`](https://ngff.openmicroscopy.org/latest/#axes-md) metadata is inferred from a DataArray by iterating over the dimensions of the array and checking for `units` and `type` properties in the attributes of the `coords` assigned to each dimension. Dimensions without coordinates will raise an exception. Scale and translation `CoordinateTransforms` are inferred by inspecting the values of the coordinates for each dimension. Be advised that no attempt is made to verify that arrays are sampled on a regular grid.\n\n## Usage\n\nGenerate `multiscales` metadata from a multiscale collection of DataArrays.\n\n```python\nfrom xarray import DataArray\nimport numpy as np\nfrom xarray_ome_ngff import create_multiscale_metadata\nimport json\ncoords = {\'z\' : DataArray(np.arange(100), attrs={\'units\': \'nm\', \'type\': \'space\'}, dims=(\'z\',)),\n         \'y\' : DataArray(np.arange(300) * 2.2, attrs={\'units\': \'nm\', \'type\': \'space\'}, dims=(\'y\')),\n         \'x\' : DataArray((np.arange(300) * .5) + 1, attrs={\'units\': \'nm\', \'type\': \'space\'}, dims=(\'x\',))}\n\ns0 = DataArray(data=0, coords=coords, dims=(\'z\',\'y\',\'x\'), name=\'s0\')\ns1 = s0.coarsen({dim: 2 for dim in s0.dims}).mean()\ns1.name = \'s1\'\n# create a small multiscale pyramid\nmultiscale = [s0, s1]\nmetadata = create_multiscale_metadata(name=\'test\', type=\'yes\', arrays=multiscale)\nprint(metadata.json(indent=2))\n```\n```json\n{\n  "version": "0.5-dev",\n  "name": "test",\n  "type": "yes",\n  "metadata": null,\n  "datasets": [\n    {\n      "path": "s0",\n      "coordinateTransformations": [\n        {\n          "type": "scale",\n          "scale": [\n            1.0,\n            2.2,\n            0.5\n          ]\n        },\n        {\n          "type": "translation",\n          "translation": [\n            0.0,\n            0.0,\n            1.0\n          ]\n        }\n      ]\n    },\n    {\n      "path": "s1",\n      "coordinateTransformations": [\n        {\n          "type": "scale",\n          "scale": [\n            2.0,\n            4.4,\n            1.0\n          ]\n        },\n        {\n          "type": "translation",\n          "translation": [\n            0.5,\n            1.1,\n            1.25\n          ]\n        }\n      ]\n    }\n  ],\n  "axes": [\n    {\n      "name": "z",\n      "type": "space",\n      "units": null\n    },\n    {\n      "name": "y",\n      "type": "space",\n      "units": null\n    },\n    {\n      "name": "x",\n      "type": "space",\n      "units": null\n    }\n  ],\n  "coordinateTransformations": [\n    {\n      "type": "scale",\n      "scale": [\n        1.0,\n        1.0,\n        1.0\n      ]\n    }\n  ]\n}\n```\n\nIt is not possible to create a DataArray from OME-NGFF metadata, but together the OME-NGFF [`Axes`](https://ngff.openmicroscopy.org/latest/#axes-md) and [`CoordinateTransformations`](https://ngff.openmicroscopy.org/latest/#trafo-md) metadata are sufficient to create _coordinates_ for a DataArray, provided you know the shape of the data. The function `create_coords` performs this operation:\n\n```python\nfrom xarray_ome_ngff import create_coords\nfrom pydantic_ome_ngff.v05.coordinateTransformations import VectorScaleTransform, VectorTranslationTransform\nfrom pydantic_ome_ngff.v05.axes import Axis\n\n\nshape = (3, 3)\naxes = [Axis(name=\'a\', units="meter", type="space"), Axis(name=\'b\', units="meter", type="space")]\n\ntransforms = [VectorScaleTransform(scale=[1, .5]), VectorTranslationTransform(translation=[1, 2])]\n\ncoords = create_coords(axes, transforms, shape)\nprint(coords)\n\'\'\'\n{\'a\': <xarray.DataArray (a: 3)>\narray([1., 2., 3.])\nDimensions without coordinates: a\nAttributes:\n    units:    meter, \'b\': <xarray.DataArray (b: 3)>\narray([2. , 2.5, 3. ])\nDimensions without coordinates: b\nAttributes:\n    units:    meter}\n\'\'\'\n```',
    'author': 'Davis Vann Bennett',
    'author_email': 'davis.v.bennett@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
