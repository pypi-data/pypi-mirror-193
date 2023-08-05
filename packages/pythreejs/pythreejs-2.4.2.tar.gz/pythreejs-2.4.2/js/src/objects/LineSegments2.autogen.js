//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var MeshModel = require('./Mesh.js').MeshModel;

var LineMaterialModel = require('../materials/LineMaterial.js').LineMaterialModel;
var LineSegmentsGeometryModel = require('../geometries/LineSegmentsGeometry.js').LineSegmentsGeometryModel;

class LineSegments2Model extends MeshModel {

    defaults() {
        return _.extend(MeshModel.prototype.defaults.call(this), {

            material: 'uninitialized',
            geometry: 'uninitialized',
            type: "LineSegments2",

        });
    }

    constructThreeObject() {

        var result = new THREE.LineSegments2(
            this.convertThreeTypeModelToThree(this.get('geometry'), 'geometry'),
            this.convertThreeTypeModelToThree(this.get('material'), 'material')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        MeshModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('material');
        this.three_properties.push('geometry');

        this.props_created_by_three['geometry'] = true;
        this.props_created_by_three['material'] = true;
        this.props_created_by_three['morphTargetInfluences'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['material'] = 'convertThreeType';
        this.property_converters['geometry'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

LineSegments2Model.model_name = 'LineSegments2Model';
LineSegments2Model.serializers = {
    ...MeshModel.serializers,
    material: { deserialize: serializers.unpackThreeModel },
    geometry: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    LineSegments2Model: LineSegments2Model,
};
