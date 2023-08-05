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

var RectAreaLightModel = require('../lights/RectAreaLight.autogen.js').RectAreaLightModel;

class RectAreaLightHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            light: null,
            color: "#ffffff",
            type: "RectAreaLightHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.RectAreaLightHelper(
            this.convertThreeTypeModelToThree(this.get('light'), 'light'),
            this.convertColorModelToThree(this.get('color'), 'color')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('light');

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['light'] = 'convertThreeType';
        this.property_converters['color'] = 'convertColor';
        this.property_converters['type'] = null;


    }
}

RectAreaLightHelperModel.model_name = 'RectAreaLightHelperModel';
RectAreaLightHelperModel.serializers = {
    ...Object3DModel.serializers,
    light: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    RectAreaLightHelperModel: RectAreaLightHelperModel,
};
