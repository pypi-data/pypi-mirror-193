//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var Object3DModel = require('../core/Object3D.js').Object3DModel;

var MaterialModel = require('../materials/Material.js').MaterialModel;
var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;
var BaseBufferGeometryModel = require('../core/BaseBufferGeometry.autogen.js').BaseBufferGeometryModel;

class MeshModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            material: [],
            geometry: null,
            drawMode: "TrianglesDrawMode",
            morphTargetInfluences: [],
            type: "Mesh",

        });
    }

    constructThreeObject() {

        var result = new THREE.Mesh(
            this.convertThreeTypeModelToThree(this.get('geometry'), 'geometry'),
            this.convertThreeTypeArrayModelToThree(this.get('material'), 'material')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_nested_properties.push('material');
        this.three_properties.push('geometry');

        this.props_created_by_three['morphTargetInfluences'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;
        this.enum_property_types['drawMode'] = 'DrawModes';

        this.property_converters['material'] = 'convertThreeTypeArray';
        this.property_converters['geometry'] = 'convertThreeType';
        this.property_converters['drawMode'] = 'convertEnum';
        this.property_converters['morphTargetInfluences'] = null;
        this.property_converters['type'] = null;

        this.property_assigners['morphTargetInfluences'] = 'assignArray';

    }
}

MeshModel.model_name = 'MeshModel';
MeshModel.serializers = {
    ...Object3DModel.serializers,
    material: { deserialize: serializers.unpackThreeModel },
    geometry: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    MeshModel: MeshModel,
};
